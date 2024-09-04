#!/usr/bin/env python

import rospy
import math
from sensor_msgs.msg import LaserScan

class LaserScanProcessor:
    def __init__(self, x_min, x_max, y_min, y_max):
        # Initialize the ROS node
        rospy.init_node('laser_listener', anonymous=True)

        # Subscribe to the /scan topic
        self.subscriber = rospy.Subscriber("/scan", LaserScan, self.callback)

        # Set region of interest boundaries
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

        # Variables to store filtered points
        self.filtered_points = []

    def callback(self, data):
        # Extract the range data and angles
        ranges = data.ranges
        angle_increment = data.angle_increment

        # Clear the previous list of filtered points
        self.filtered_points.clear()

        # Loop through the ranges and process each one
        for i, range_value in enumerate(ranges):
            if not math.isnan(range_value) and not math.isinf(range_value):
                # range (θ = i * Δθ)
                angle = i * angle_increment

                # polar coordinates (r, θ) to Cartesian coordinates (x, y)
                x, y = self.polar_to_cartesian(angle, range_value)

                # Check if the point is within the region of interest (ROI)
                if self.is_in_roi(x, y):
                    self.filtered_points.append((x, y))

        # Calculate and display the mean of x and y coordinates
        if self.filtered_points:
            mean_x, mean_y = self.calculate_mean()
            rospy.loginfo(f"Mean x: {mean_x}, Mean y: {mean_y}")

    def polar_to_cartesian(self, angle, range_data):
        #  polar coordinates to Cartesian coordinates
        x = range_data * math.cos(angle)
        y = range_data * math.sin(angle)
        return x, y

    def is_in_roi(self, x, y):
        # Check if the point is within the region of interest
        return self.x_min <= x <= self.x_max and self.y_min <= y <= self.y_max

    def calculate_mean(self):
        # Calculate the mean of the x and y coordinates
        sum_x = sum(point[0] for point in self.filtered_points)
        sum_y = sum(point[1] for point in self.filtered_points)
        mean_x = sum_x / len(self.filtered_points)
        mean_y = sum_y / len(self.filtered_points)
        return mean_x, mean_y

    def run(self):
        # Keep the node running
        rospy.spin()

if __name__ == '__main__':
    try:
        # Define region of interest (ROI) boundaries

        x_min, x_max = -1.0, 1.0  
        y_min, y_max = -1.0, 1.0  

        # Create the LaserScanProcessor object with the specified ROI

        processor = LaserScanProcessor(x_min, x_max, y_min, y_max)
        
        # Run the processor
        processor.run()
    except rospy.ROSInterruptException:
        pass
