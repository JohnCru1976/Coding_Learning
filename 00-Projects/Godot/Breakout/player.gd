extends RigidBody2D

var left_force = 0
var right_force = 0
var speed = 500

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
	
func _physics_process(delta):
	if Input.is_action_pressed("left"):
		set_linear_velocity(Vector2(-speed, get_linear_velocity().y))
	elif Input.is_action_pressed("right"):
		set_linear_velocity(Vector2(speed, get_linear_velocity().y))
	else:
		set_linear_velocity(Vector2(0, get_linear_velocity().y))
	
	
