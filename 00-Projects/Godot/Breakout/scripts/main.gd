extends Node

@export var star_scene: PackedScene
@export var ball_scene: PackedScene
@export var brick_scene: PackedScene

var initial_player_position = Vector2(240,690)
var background_stars = 70
var bricks = 0

# Called when the node enters the scene tree for the first time.
func _ready():
	$HUD.start_game.connect($BrickDistribution._on_start_button)
	# Spawn player position
	$Player.position = initial_player_position
	
	# Background stars
	spawn_stars()
	

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func spawn_ball():
		var ball = ball_scene.instantiate()
		add_child(ball)
		# Connection with ball_lost in signal
		ball.ball_lost.connect($HUD._on_ball_lost)
		
		
func spawn_stars():
	# Stars distribution
	for i in range(0,background_stars):
		var star = star_scene.instantiate()
		add_child(star)
		

func start():
	# Spawn ball
	spawn_ball() 
	
func brick_broken():
	bricks -= 1
	print(bricks)


func _on_brick_distribution_next_level(level_num):
	$Ball.queue_free()
	$HUD.set_level(level_num)

func _on_brick_distribution_emit_success():
	$Ball.queue_free()
