extends Area2D

@export var player_num: int # The player number of the instance
var speed = 600				# Initial speed
var stick_direction = 0		# Direcction -1 = Up  1 = Down
var player_scale = 0.5
var ball_collision = false
# Offset limits on the screen
var gap_left = 20
var gap_right = 55
var gap_down = 135
# Takes the screen dimensions
var screen_width
var screen_height
# Active shape
var active_shape = -1

# Called when the node enters the scene tree for the first time.
func _ready():
	# Getting and setting screen parameters
	start_screen_parameters()
	# Setting player
	start_position_player()

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	# Initial direction of movement
	var movement = Vector2.ZERO
	stick_direction = 0
	# Keys responsive
	if Input.is_action_pressed("p" + str(player_num) + "_up"):
		movement.y -= 1
		stick_direction = -1
	if Input.is_action_pressed("p" + str(player_num) + "_down"):
		movement.y += 1
		stick_direction = 1
	# Setting the position
	position += movement.normalized() * speed * delta
	limits_screen_player()
	
func _on_area_shape_entered(area_rid, area, area_shape_index, local_shape_index):
	# Avoid double area touched
	if active_shape >= 0:
		return
	# Actual area active
	active_shape = local_shape_index
	# Actions on ball
	if area:
		if area.has_method("get_name") and area.get_name() == "Ball":
			# The collisioned object is the ball
			# Initialize actions in Ball			
			area.stick_collision(player_num, local_shape_index, stick_direction)
			$Timer.start()
			
func start_position_player():
	#Initial Position
	if player_num == 1:
		#Initial Position
		position = Vector2(gap_left, screen_height / 2 - gap_down / 2)
	if player_num == 2:
		#Initial Position
		position = Vector2(screen_width - gap_right, screen_height / 2 - gap_down / 2)
		
func limits_screen_player():
	if player_num == 1:
		# Screen limits
		position = position.clamp(Vector2(gap_left, 0),
					Vector2(gap_left, screen_height - gap_down))
	if player_num == 2:
		# Screen limits
		position = position.clamp(Vector2(screen_width - gap_right, 0),
					Vector2(screen_width - gap_right, screen_height - gap_down))

func start_screen_parameters():
	# Screen dimensions parameters
	screen_width = get_viewport().size.x
	screen_height = get_viewport().size.y
	# Reducing the escale
	scale = Vector2(player_scale, player_scale)
	
func _on_timer_timeout():
	active_shape = -1 
