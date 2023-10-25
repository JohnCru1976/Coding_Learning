extends AnimatedSprite2D

var is_big_stick = true

func _ready():
	pass
	
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

### TEST WITH ANIMATION ###
func animation_example():
	var tween = create_tween()
	if is_big_stick == true:
		tween.tween_property(self, "scale", Vector2(0.3,0.5), 1)
		tween.parallel().tween_property(self, "rotation", 2 * PI, 1)
		is_big_stick = false
	elif is_big_stick == false:
		tween.tween_property(self, "scale", Vector2(0.7,0.5), 1)
		tween.parallel().tween_property(self, "rotation", - 2 * PI, 1)
		is_big_stick = true
	print(is_big_stick)
	$Timer.start()
	
func _on_timer_timeout():
	animation_example()
