extends Line2D

# Takes the screen dimensions
var screen_width
var screen_height

# Called when the node enters the scene tree for the first time.
func _ready():
	# Screen dimensions parameters
	screen_width = get_viewport().size.x
	screen_height = get_viewport().size.y
	# Setting the points that draw the line
	var initial_point = Vector2(screen_width / 2, 0)
	var final_point =  Vector2(screen_width / 2, screen_height)
	# Setting the middle line
	clear_points()
	width = 1
	add_point(initial_point, 0)
	add_point(final_point, 1)

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
