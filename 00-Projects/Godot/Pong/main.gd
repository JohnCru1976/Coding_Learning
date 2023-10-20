extends Node

@export var ball_scene: PackedScene
var screen_width
var screen_height

# Called when the node enters the scene tree for the first time.
func _ready():
	$HUD.scores = [0,0]
	screen_width = get_viewport().size.x
	screen_height = get_viewport().size.y
	
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if Input.is_action_pressed("exit"):
		# Window closed
		get_tree().quit()
		
func _on_start_timer_timeout():
	start_ball()

func start_ball():
	var ball = ball_scene.instantiate()
	ball.screen_width = screen_width
	ball.screen_height = screen_height
	# Spawn the ball by adding it to the Main scene.
	add_child(ball)

func sum_point(num_player):
	if num_player == 1:
		$HUD.scores = [$HUD.scores[0] + 1, $HUD.scores[1]]
	if num_player == 2:
		$HUD.scores = [$HUD.scores[0], $HUD.scores[1] + 1]
	
	if $HUD.scores[1] >= 5 or $HUD.scores[0] >= 5:
		$HUD.start()
	else:
		$StartTimer.start()


