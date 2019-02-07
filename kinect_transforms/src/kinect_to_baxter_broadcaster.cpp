#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <string.h>
/**
 * @file
 */
    
/**
 * Main function: 
 * a TF broadcaster is created in order to add the world frame to the tree. The world frame is in correspondence of the control board and it has the same orientation of the Kinect.
 */
int main(int argc, char** argv)
{
    ros::init(argc, argv, "kinect_broadcaster");
	ros::NodeHandle n("~");
	
	std::string fixed_frame_kinect;
	std::string fixed_frame_baxter;
	
	double x_frame_kinect, y_frame_kinect, z_frame_kinect;
	// position of the Kinect with respect to the control board
	n.param<std::string>("fixed_frame_baxter", fixed_frame_baxter, "world");
	n.param<std::string>("fixed_frame_kinect", fixed_frame_kinect, "world_frame");
	n.param<double>("x_frame_kinect", x_frame_kinect, 0.0);
	n.param<double>("y_frame_kinect", y_frame_kinect, 0.0);
	n.param<double>("z_frame_kinect", z_frame_kinect, 0.0);
	
	ros::Rate r(10000);
	tf::TransformBroadcaster broadcaster;
	
    tf::Transform change_frame(tf::Quaternion(0, 0, 0, 1), tf::Vector3(x_frame_kinect, y_frame_kinect, z_frame_kinect));

    
	while(ros::ok()){
		broadcaster.sendTransform(tf::StampedTransform(change_frame, ros::Time::now(), fixed_frame_baxter, fixed_frame_kinect));
		r.sleep();
	}

    return 0;
}
