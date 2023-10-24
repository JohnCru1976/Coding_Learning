extends AnimatedSprite2D

# Called when the node enters the scene tree for the first time.
func _ready():
	
	pass
	
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

### TEST WITH ANIMATION ###
func animation_destruction():
	var tween = create_tween()
	
	#tween.tween_property(self, "scale", Vector2(2.5,2.5), 0.2)
	tween.tween_property(self, "scale", Vector2(0.0,0.0), 0.2)
	tween.parallel().tween_property(self, "rotation", 4 * PI, 0.2)
	
	
