extends Node

@export var ball_scene: PackedScene

# Called when the node enters the scene tree for the first time.
func _ready():
	$StartTimer.start()
	
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if Input.is_action_pressed("exit"):
		# Window closed
		get_tree().quit()
		
func _on_start_timer_timeout():
	start_ball()

func start_ball():
	var ball = ball_scene.instantiate()
	# Spawn the ball by adding it to the Main scene.
	add_child(ball)
