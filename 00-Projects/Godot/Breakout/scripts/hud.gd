extends CanvasLayer

signal start_game

var game_time = 0
var count_down = 3
var first_time = true
var record = 0
var lifes = 3
var bola_lanzada = false
var success = false


# Called when the node enters the scene tree for the first time.
func _ready():
	start_lifes()
	stop()
	record = load_record()


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	$Score.text = str("Tiempo: ", seconds_to_minutes(game_time))
	if record == 0:
		$Record.text = str("Record\n- -")
	else:
		$Record.text = str("Record\n", seconds_to_minutes(record))
func stop():
	$GameTime.stop()
	# The player get over all the levels
	if success == true:
		if (record == 0 or game_time < record) and first_time == false:
			record = game_time
			save_record(record)
			$Message.text = "¡¡Nuevo record!!"
			$Message.visible = true
	else:
		if first_time == false:
			$Message.text = "Game Over"
			$Message.visible = true
		else:
			$Message.visible = false
			
	$Button.visible = true
		
func start():
	start_lifes()
	game_time = 0
	count_down = 3
	$Level.text = str("Level 1")
	$Button.visible = false
	$GameTime.start()
	
	
func life_lost():
	lifes -= 1
	if lifes == 2:
		$Lifes/Life3.visible = false
	if lifes == 1:
		$Lifes/Life2.visible = false
	if lifes == 0:
		$Lifes/Life1.visible = false
		stop()
		
func start_lifes():
	lifes = 3
	$Lifes/Life1.visible = true
	$Lifes/Life2.visible = true
	$Lifes/Life3.visible = true

func seconds_to_minutes(seconds):
	# Param: seconds: int
	# Return: time in format mm/ss: string 
	var seconds_format = seconds % 60
	var minutes_format = (seconds - seconds_format) / 60
	if minutes_format < 10:
		minutes_format = str("0", minutes_format)
	if seconds_format < 10:
		seconds_format = str("0", seconds_format)
	return str(minutes_format, ":", seconds_format)
	
func load_record():
	if not FileAccess.file_exists("user://breakout_savegame.save"):
		return 0
	
	var save_score = FileAccess.open("user://breakout_savegame.save", FileAccess.READ)
	save_score.get_position()
	var record_saved = int(save_score.get_line())
	
	return record_saved
	
func save_record(score):
	var save_record = FileAccess.open("user://breakout_savegame.save", FileAccess.WRITE)
	if save_record:
		save_record.store_line(str(score))

func _on_game_time_timeout():
	if count_down < 0:
		if bola_lanzada == false:
			get_parent().start()
			bola_lanzada = true
		$Message.visible = false
		game_time += 1
		
	elif count_down == 0:
		$Message.visible = true
		$Message.text = str("¡¡Vamos!!!")
		count_down -= 1
		bola_lanzada = false
	elif count_down > 0:
		$Message.visible = true
		$Message.text = str(count_down)
		count_down -= 1
		bola_lanzada = false
		
func _on_button_pressed():
	start()
	first_time = false
	success = false
	start_game.emit()

func _on_ball_lost():
	count_down = 3
	life_lost()
	
func set_level(num):
	$Level.text = str("Nivel ", num)
	if num == 3:
		$Level.text = str("Nivel 3 (Designed by Juan)")
	count_down = 3
	
func _on_brick_distribution_emit_success():
	success = true
	stop() 


	
