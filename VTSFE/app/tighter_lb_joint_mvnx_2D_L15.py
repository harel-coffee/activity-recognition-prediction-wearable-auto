from .models.tighter_lb_2D import Tighter_LB_2D

tighter_lb_joint_mvnx_2D_L15 = Tighter_LB_2D()
tighter_lb_joint_mvnx_2D_L15.set_data_config(["jointAngle"], "MVNX")

tighter_lb_joint_mvnx_2D_L15.DMP_PARAMS["model_monte_carlo_sampling"] = 15
