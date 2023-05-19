from typing import List
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Point
from tf.transformations import euler_from_quaternion
from time import sleep
import math
from fila import Fila

class TurtleController(Node):
    def __init__(self):
        
        super().__init__('turtle_controller')
        self.publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.move_turtle)
        self.msg = Twist()
        self.queue = Fila()
        
        self.queue.trajetoria((0.0, 0.5))
        self.queue.trajetoria((0.5, 0.0))
        self.queue.trajetoria((0.0, 0.5))
        self.queue.trajetoria((0.5, 0.0))
        self.queue.trajetoria((0.0, 1.0))
        self.queue.trajetoria((1.0, 0.0))



    def move_turtle(self):
        if not self.queue.vazia():
            x, y = self.queue.desenfileirar()
            self.msg.linear.x = x
            self.msg.angular.z = y
            self.publisher.publish(self.msg)
            sleep(1.0)
        else:
            self.msg.linear.x = 0.0
            self.msg.angular.z = 0.0
            self.publisher.publish(self.msg)
            sleep(1.0)
            exit()

def main(args=None):
    
    rclpy.init(args=args)
    turtle_controller = TurtleController()
    rclpy.spin(turtle_controller)
    turtle_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()