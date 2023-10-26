extends StaticBody2D

signal brick_broken
# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func _on_timer_timeout():
	queue_free()

func kill_instance():
		brick_broken.emit()
		$CollisionShape2D.disabled = true
		$AnimatedSprite2D.animation_destruction()
		$Timer.start()
		
func _on_start_button():
	queue_free()
