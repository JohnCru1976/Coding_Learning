extends StaticBody2D

signal brick_broken

@export var brick_color: int

# Called when the node enters the scene tree for the first time.
func _ready():
	pass

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func _on_timer_timeout():
	queue_free()

func kill_instance():
		brick_broken.emit()
		$AnimatedSprite2D.visible = false
		$CollisionShape2D.disabled = true
		explosion()
		$Timer.start()
		
func _on_start_button():
	queue_free()
	
func explosion():
	if brick_color == 0:
		$Explosion.process_material.color = Color.BLUE
	if brick_color == 1:
		$Explosion.process_material.color = Color.CYAN
	if brick_color == 2:
		$Explosion.process_material.color = Color.GREEN
	if brick_color == 3:
		$Explosion.process_material.color = Color.PURPLE
	if brick_color == 4:
		$Explosion.process_material.color = Color.RED
	if brick_color == 5:
		$Explosion.process_material.color = Color.YELLOW
	$ExplosionSound.play()
	$Explosion.emitting = true
