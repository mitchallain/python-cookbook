A brief action client implementation

```python
import actionlib

from vision_msgs.msg import DetectObjectsAction, DetectObjectsGoal, DetectObjectsFeedback
# Note there is also a DetectObjectsActionFeedback, it is put there to confuse us


def detect_objects_feedback_cb(self, feedback: DetectObjectsFeedback):
    status = feedback.status


def main():
    ac = actionlib.SimpleActionClient(action_name, DetectObjectsAction)

    goal = DetectObjectsGoal()
    ac.send_goal(goal, feedback_cb=detect_objects_feedback_cb)

    if not ac.wait_for_result(
            rospy.Duration(self.detect_timeout_sec)):
        rospy.logerr("detection request timed out")
        return

    result = self.detect_objects_ac.get_result()
```

# References
- [actionlib](http://wiki.ros.org/actionlib)
- [actionlib Tutorials](http://wiki.ros.org/actionlib_tutorials/Tutorials/Writing%20a%20Simple%20Action%20Client%20%28Python%29)
- [Foxglove Blog - Creating ROS 1 Actions](https://foxglove.dev/blog/creating-ros1-actions)
