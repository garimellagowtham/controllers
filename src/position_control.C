#include "ros/ros.h"
#include <tf/transform_broadcaster.h>
#include <tf/transform_listener.h>
#include "SetptCtrl.h"
using namespace std;

ros::Subscriber currframe_sub;
ros::Subscriber usergains_sub;
ros::Subscriber goalpoint_sub;

SetptCtrl *setptctrlinst;//forward declaration of pointer

int main(int argc, char **argv)
{
	ros::init(argc,argv,"position_control");
	ros::NodeHandle posnctrl("/pctrl");
	setptctrlinst = new SetptCtrl(&posnctrl);
	//configure setptctrl
	setptctrlinst->kpr = 2.7;
	setptctrlinst->kdr = 2.0;
	setptctrlinst->kpt = 0.8;
	setptctrlinst->kdt = 0.7;
	setptctrlinst->cbatt = 5.0;

	currframe_sub = posnctrl.subscribe("pose",1,&SetptCtrl::Set,setptctrlinst);
	usergains_sub = posnctrl.subscribe("gains",1,&SetptCtrl::setgains,setptctrlinst);
	goalpoint_sub = posnctrl.subscribe("goal",1,&SetptCtrl::setgoal,setptctrlinst);
	ros::spin();

	return 0;
}
