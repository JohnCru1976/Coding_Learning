extends CharacterBody2D

signal ball_lost

var direction		# Is a normalized 2D vector
var speed = 300		# Initial speed
var offset = 5
# Screen parameters
var screen_width = 480
var screen_height = 720
var limits_bounce = false
var failure = false

# Called when the node enters the scene tree for the first time.
func _ready():
	start_ball()

func _physics_process(delta):
	var normal_direction = direction.normalized()
	print(normal_direction)
	# Move the object on the actual direction
	var collision = move_and_collide(direction.normalized() * speed * delta)
	if collision:
		var type_collision = collision.get_collider().get_class()
		# Player collision
		if type_collision == "AnimatableBody2D":
			# Control the impact with the stick
			stick_collision(collision)
		# Brick collision
		if type_collision == "StaticBody2D":
			var direction_after = direction.bounce(collision.get_normal())
			var brick = collision.get_collider()
			# Avoid excessive angle
			if absf(direction_after.y) <= 0.3:
				direction_after.y = (direction_after.y / abs(direction_after.y)) * 0.3
			direction = direction_after
			brick.kill_instance()
			
	# Screen top limits
	if position.y <= 0 + offset:
		position.y = 10
		direction.y = - direction.y
		$BounceWall.play()
	# Screen bottom limits
	if position.y >= screen_height + 50:
		## TODO: La bola toca la parte inferior ##
		if failure == false:
			$Failure.play()
			$TimerFailure.start()
			failure = true
	# Screen lef-rigth limits
	if position.x <= 0 + offset:
		position.x = offset + 3
		direction.x = - direction.x
		$BounceWall.play()
	if position.x >= screen_width - offset:
		position.x = screen_width - offset - 3
		direction.x = - direction.x
		$BounceWall.play()
		
	
# The ball collisions with stick
func stick_collision(collision):
	var stick = collision.get_collider()	
	var stick_direction = stick.get_player_direction()
	var direction_before = direction		
	var direction_after = direction.bounce(collision.get_normal())
	# Global point collision in stick
	var global_point_collision = collision.get_position()
	# Global point collision in stick 
	var stick_point_collision = stick.to_local(global_point_collision)
	# Stick left extreme
	if stick_point_collision.x <= -15:
		if  direction_before.x > 0 and direction_after.x > 0:
			direction_after.x *= -1
			if stick_direction == 1:
				speed += 5
			if stick_direction == -1:
				speed += 15
	# Stick rigth extreme
	if stick_point_collision.x >= 15:
		if  direction_before.x < 0 and direction_after.x < 0:
			direction_after.x *= -1 
			speed += 10
			if stick_direction == 1:
				speed += 15
			if stick_direction == -1:
				speed += 5
	# Response to stick direction
	if direction_before.x > 0 and direction_after.x > 0: # Right - No reverse x
		if stick_direction == 1:
			direction_after.x += 0.2
			speed += 15
		if stick_direction == -1:
			direction_after.x -= 0.2
			direction_after.y -= 0.2
			speed -= 15
	if direction_before.x < 0 and direction_after.x < 0: # Left - No reverse x
		if stick_direction == 1:
			direction_after.x += 0.2
			direction_after.y -= 0.2
			speed -= 15
		if stick_direction == -1:
			direction_after.x -= 0.2
			speed += 15
	# Avoid excessive angle
	if absf(direction_after.y) <= 0.3:
		direction_after.y = (direction_after.y / abs(direction_after.y)) * 0.7
		direction_after.x = (direction_after.x / abs(direction_after.x)) * 0.2
	# Applying new direction
	direction = direction_after
	$BounceStick.play()
	speed += 10
			
func start_ball():
	# Inicializa la posición
	position = Vector2(screen_width / 2, screen_height / 2 + 35)
	# Inicializa la dirección - Sale hacia abajo con un angulo aleatorio
	direction = Vector2( random_number(-0.5, 0.5), 1)
	
func random_number(num_min, num_max):
	# Generate a random number between min_value (inclusive) and max_value (exclusive)
	var random_number = randf() * (num_max - num_min) + num_min
	return random_number
	

func _on_timer_failure_timeout():
	ball_lost.emit()
	queue_free()
	failure = false
