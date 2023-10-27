extends AnimatableBody2D

var dragging = false
var initial_offset
var player_position = Vector2(240,620)
var player_direction = 0  # 1 Right  -1 Left

func _ready():
	pass

func _input(event):
	if event is InputEventMouseButton:
		var mouse_event = event as InputEventMouseButton
		if mouse_event.button_index == MOUSE_BUTTON_LEFT:
			if mouse_event.is_pressed():
				if global_position.distance_to(mouse_event.position) < 100: # Define un umbral de proximidad
					dragging = true
					initial_offset = global_position - mouse_event.position
			elif mouse_event.is_released():
				dragging = false
				player_direction = 0
				

func _physics_process(delta):
	global_position = player_position
	# Spawn player position
	

	if dragging:
		var global_mouse = get_global_mouse_position()
		var new_position = global_mouse + initial_offset
		if new_position.x > player_position.x:
			player_direction = 1
		elif new_position.x < player_position.x:
			player_direction = -1
		else:
			player_direction = 0
		if new_position.x < 0:
			new_position.x = 0
		if new_position.x > 480:
			new_position.x = 480
		player_position.x = new_position.x

func get_player_direction():
	return player_direction
	
