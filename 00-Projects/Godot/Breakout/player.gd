extends RigidBody2D

var left_force = 0
var right_force = 0
var speed = 500
var touched = false
var width = 92.727
var height = 21.184

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
		
	if touched:
		pass
		# Actualiza la posición del RigidBody2D en función del toque
		#position = get_parent().get_local_mouse_position()
		
func _input(event):
	# Mouse touch detection
	if event is InputEventScreenTouch:
		var touch = event as InputEventScreenTouch
		if touch.pressed and is_point_inside(to_local(touch.position)):
			touched = true
		else:
			touched = false

func is_point_inside(point):
	if point.x >= - width  and point.x <= width:	
		if point.y >= - height and point.y <= height :		
			return true
		
	return false
	
