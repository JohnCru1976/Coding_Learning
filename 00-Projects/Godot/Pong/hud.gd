extends CanvasLayer

@export var scores: Array

# Called when the node enters the scene tree for the first time.
func _ready():
	scores = [0, 0]
	$Button.visible = true
	$Message.visible = false

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	$Player1.text = str(scores[0])
	$Player2.text = str(scores[1])
	
func start():
	$Button.visible = true
	$Message.visible = true

func _on_button_pressed():
	scores = [0, 0]
	$Button.visible = false
	$Message.visible = false
	var ball_timer = get_parent().get_node("StartTimer")
	ball_timer.start()

