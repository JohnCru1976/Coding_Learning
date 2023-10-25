extends AnimatableBody2D

var dragging = false
var initial_offset
var player_position = Vector2(240,690)

func _input(event):
	if event is InputEventMouseButton:
		var mouse_event = event as InputEventMouseButton
		if mouse_event.button_index == MOUSE_BUTTON_LEFT:
			if mouse_event.is_pressed():
				if global_position.distance_to(mouse_event.position) < 30: # Define un umbral de proximidad
					dragging = true
					initial_offset = global_position - mouse_event.position
			elif mouse_event.is_released():
				dragging = false

func _physics_process(delta):
	global_position = player_position

	if dragging:
		var global_mouse = get_global_mouse_position()
		var new_position = global_mouse + initial_offset
		player_position.x = new_position.x

		

	
