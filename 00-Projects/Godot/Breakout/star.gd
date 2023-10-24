extends AnimatedSprite2D

# Called when the node enters the scene tree for the first time.
func _ready():
	# Random position
	var x_min = 5
	var x_max = 475
	var y_min = 5
	var y_max = 715
	position.x = randi() % (x_max - x_min + 1) + x_min
	position.y = randi() % (y_max - y_min + 1) + y_min
	
	# Timer initial time
	var time_min = 0.05
	var time_max = 0.6
	var random_time = randf() * (time_max - time_min) + time_min
	$Timer.wait_time = random_time
	$Timer.start()
	
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func _on_timer_timeout():
	play("change_color")
	visible = true
