extends StaticBody2D

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func _on_timer_timeout():
	queue_free()

func _on_area_shape_entered(area_rid, area, area_shape_index, local_shape_index):
	var ball_position = area.position
	var brick_position = self.position
	if area.get_name() == "Ball":
		$AnimatedSprite2D.animation_destruction()
		$Timer.start()
		print(collision_side(ball_position, brick_position))
		
func collision_side(ball_position, brick_position):
			pass
		
