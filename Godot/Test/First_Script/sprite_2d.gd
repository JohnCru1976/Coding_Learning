extends Sprite2D

var speed = 400
var angular_speed = PI

# Custom signal example
# Object of type signal declaration
signal health_changed(old_value, new_value)
# Initial health variable
var health = 10

func _init():
	print("Hola Mundo!")
func _ready():
	var timer = get_node("Timer")
	timer.timeout.connect(_on_timer_timeout)
	# Important: this is a custom signal connection
	self.health_changed.connect(on_health_depleted)

func _process(delta):
	''' Delta makes our motion independent of our framerate
	# Delta is returned when we call the method _process from the Node class 
	# Rotation and position are properties inherited from the class Node2D,
	# which Sprite2D extends. '''
	
	var direction = 0
	if Input.is_action_pressed("ui_left"):
		direction = -1
	if Input.is_action_pressed("ui_right"):
		direction = 1
	
	rotation += angular_speed * direction * delta
	
	var velocity = Vector2.ZERO
	if Input.is_action_pressed("ui_up"):
		velocity = Vector2.UP.rotated(rotation) * speed

	position += velocity * delta

# The sprite receives damage
func take_damage(amount):
	var old_health = health
	health -= amount
	print("Healt :" + str(old_health))
	if health <= 0:
		# This method emits a signal
		health_changed.emit(old_health, health)

# This method receives the signal of take_damage(amount)
# when health <= 0
func on_health_depleted(old_value, new_value):
	print("Your live is gone")
	print("Old value: " + str(old_value), " New value: " + str(new_value))
	
# Deactivate the process method
# This function receive the signal
func _on_button_pressed():
	set_process(not is_processing())
	take_damage(1)

# The sprite turns visible every timeout
# This function receive the signal
func _on_timer_timeout():
	visible = not visible
	

