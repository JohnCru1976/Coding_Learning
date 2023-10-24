extends Node

@export var star_scene: PackedScene
@export var ball_scene: PackedScene
@export var brick_scene: PackedScene

var initial_player_position = Vector2(240,690)
var background_stars = 70

# Called when the node enters the scene tree for the first time.
func _ready():
	# Spawn player position
	$Player.position = initial_player_position
	# Background stars
	spawn_stars()
	# Spawn ball
	spawn_ball()
	# TESTS #

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func spawn_ball():
		var ball = ball_scene.instantiate()
		add_child(ball)
		
func spawn_stars():
	# Stars distribution
	for i in range(0,background_stars):
		var star = star_scene.instantiate()
		add_child(star)
	
