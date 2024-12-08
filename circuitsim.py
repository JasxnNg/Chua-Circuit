Web VPython 3.2
# need a way to reset 
# need user input 
# need other things as well 

# need runge-kutta differential equations

g1_g = graph(title = "Graph of x", width = 400, height = 400, align = "right")
g2_g = graph(title = "Graph of y", width = 400, height = 400, align = "right")
g3_g = graph(title = "Graph of z", width = 400, height = 400, align = "right")

scene = canvas(width=600, height=600, align = "left") # init canvas 
scene.camera.pos = vector(0, 0, 1)
scene.center = vector(5, 0, 0)  # the object is centered at (0, 0, 0) for convienence
scene.userspin = False  # restrict it to be practically 2D
scene.userzoom = False  # stop the user from zooming too far in/out
scene.autoscale = False
scene.range = 7


inductor = helix(pos=vec(-1, 0, 0), axis=vec(0, 1, 0), color=color.red, radius=0.5) 
ind_1_connect = curve(pos=[vec(- 1, 1, 0), vec(-1, 3, 0), vec(2, 3, 0)], color=color.yellow)
ind_2_connect = curve(pos=[vec(- 1, 0, 0), vec(-1, -2, 0), vec(2, -2, 0)], color=color.yellow)
cap_1_c1 = curve(pos=[vec(2, 3, 0), vec(2, 0.75, 0)], color=color.yellow)
cap_1_c2 = curve(pos=[vec(2, 0.25, 0), vec(2, -2, 0)], color=color.yellow)
cap_1_t = curve(pos=[vec(1.5, 0.75, 0), vec(2.5, 0.75, 0)], color=color.red)
cap_1_b = curve(pos=[vec(1.5, 0.25, 0), vec(2.5, 0.25, 0)], color=color.red)

cap_2_c1 = curve(pos=[vec(5, 3, 0), vec(5, 0.75, 0)], color=color.yellow)
cap_2_c2 = curve(pos=[vec(5, 0.25, 0), vec(5, -2, 0)], color=color.yellow)
cap_2_t = curve(pos=[vec(4.5, 0.75, 0), vec(5.5, 0.75, 0)], color=color.red)
cap_2_b = curve(pos=[vec(4.5, 0.25, 0), vec(5.5, 0.25, 0)], color=color.red)
cap_2_c1 = curve(pos=[vec(5, 3, 0), vec(5, 0.75, 0)], color=color.yellow)
cap2_connect_1 = curve(pos=[vec(5, 3, 0), vec(5, 0.75, 0)], color=color.yellow)
cap2_connect_2 = curve(pos=[vec(2, -2, 0), vec(9, -2, 0)], color=color.yellow)

var_resistor_2_c = curve(pos=[vec(9,2,0), vec(9,3,0), vec(4,3,0)], color = color.yellow)
var_resistor_3_c = curve(pos=[vec(2,3,0), vec(3,3,0)], color = color.yellow) 


#diode_resis_1 = curve(pos=[vec(7,5,0), vec(7,1,0)], color = color.yellow)

def draw_resistor(start_pos, orientation = "horizontal", scale = 1):
    start_x = start_pos.x
    start_y = start_pos.y
#    print(type(start_pos))
    start_z = start_pos.z
    arr = []
    cur_arr = [start_pos]
    for i in range(5):
        arr.append(-1 * 0.2 if i != 0 else 0)
    
    for index, val in enumerate(arr):
        if orientation == "horizontal":
            new_vec = vec(start_x + index * 0.2 , start_y + abs(val)*scale, start_z)
            cur_arr.append(new_vec)
            new_vec = vec(start_x + index * 0.2 , start_y + val*scale, start_z)
            cur_arr.append(new_vec)
        else: 
            new_vec = vec(start_x + abs(val)*scale, start_y + index * 0.2 , start_z)
            cur_arr.append(new_vec)
            new_vec = vec(start_x + val*scale, start_y + index * 0.2, start_z)
            cur_arr.append(new_vec)

    if orientation == "horizontal":     
        cur_arr.append(vec(start_x + (index + 1) * 0.2, start_y, start_z))
    else:
        cur_arr.append(vec(start_x, start_y + (index + 1) * 0.2, start_z))
#    print(cur_arr)
    
    return cur_arr
    
    
    
#resis = draw_resistor(vec(3,3,0))
#start = vec(0,0,0)
#pos_arr = draw_resistor(start)
resistor = curve(pos = draw_resistor(vec(3,3,0)), color = color.red)


var_diode = curve(pos=[vec(8.5,2,0), vec(9.5,2,0)], color = color.yellow)
resis_1 = curve(pos = draw_resistor(vec(7.5,2,0)), color = color.red)
resis_2 = curve(pos = draw_resistor(vec(9.5,2,0)), color = color.red)
corner = curve(pos=[vec(7.5,0,0), vec(7,0,0), vec(7,2,0), vec(7.5,2,0)], color = color.yellow)

line_connecting_diode = curve(pos=[vec(7,1,0), vec(7.5,1,0)], color = color.yellow)
diode = pyramid(pos=vec(8.5, 1, 0), axis=vec(-1, 0, 0), color=color.green, width = 0.1, height = 0.85)
l2_diode = curve(pos=[vec(8.5,1.25,0), vec(8.75,1.25,0), vec(8.75,2,0)], color = color.yellow)
l3_diode = curve(pos=[vec(8.5,0.75,0), vec(8.75,0.75,0), vec(8.75,-0.5,0)], color = color.yellow)

#line = curve(pos=[vec(8.5, 0, 0), vec(9.5, 0, 0)], color = color.yellow)
resis_3 = curve(pos = draw_resistor(vec(7.5,0,0)), color = color.red)
resis_4 = curve(pos = draw_resistor(vec(9.5,0,0)), color = color.red)
corner = curve(pos=[vec(10.5,0,0), vec(11,0,0), vec(11,2,0), vec(10.5,2,0)], color = color.yellow)
line_connecting_diode = curve(pos=[vec(11,1,0), vec(10.5,1,0)], color = color.yellow)

diode = pyramid(pos=vec(9.5, 1, 0), axis=vec(1, 0, 0), color=color.green, width = 0.1, height = 0.85)
l2_diode = curve(pos=[vec(9.5,1.25,0), vec(9.25,1.25,0), vec(9.25,2,0)], color = color.yellow)
l3_diode = curve(pos=[vec(9.5,0.75,0), vec(9.25,0.75,0), vec(9.25,-0.5,0)], color = color.yellow)

connect_bottom1 = curve(pos=[vec(9.5,0,0), vec(9.25,0,0)], color = color.yellow)
connect_bottom2 = curve(pos=[vec(8.5,0,0), vec(8.75,0,0)], color = color.yellow)
resistor_f1 = curve(pos = draw_resistor(vec(8.75,-1.5,0), "vertical", 0.8), color = color.red)
resistor_f2 = curve(pos = draw_resistor(vec(9.25,-1.5,0), "vertical", 0.8), color = color.red)
final = curve(pos = [vec(8.75,-1.5,0), vec(8.75,-2,0)], color = color.yellow)
final = curve(pos = [vec(9.25,-1.5,0), vec(9.25,-2,0), vec(9,-2,0)], color = color.yellow)



m0 = -1.143
m1 = -0.714
fun_arr = [0.3, 0, 0]

alpha_beta = [15.6, 28]
time_dt = [0, 0.01]




#clear everything by removing them from the graphics processing thingy-ma-bob 
#then, delete it 
def clear(b): 
    g1.delete()
    g2.delete()
    g3.delete()
#
    time_dt[0] = 0  
    fun_arr[0] = 0.3 
    fun_arr[1] = 0
    fun_arr[2] = 0

#this is a button to restart (cannot be radio) 
button(text="Restart", 
       pos=scene.title_anchor, 
       bind = clear )
    
#dummy method to just do nothing :-) 
def do_nothing(ev):
    pass

def surface_loop_toggle(ev):

    loop_toggle.checked = not surface_toggle.checked 
    currSlider.disabled = False 
    anotherSlider.disabled = False 
    clear() #clears everything else 

def loop_toggle(ev): 
    surface_toggle.checked = not loop_toggle.checked 
    currSlider.value = 15.6
    anotherSlider.value = 28 
    currSlider.disabled = True
    anotherSlider.disabled = True
    wt1.text = '{:1.2f} alpha\n'.format(currSlider.value)
    wt2.text = '{:1.2f} beta\n'.format(anotherSlider.value)
    clear()

#--------Define all the buttons that we have----- 
loop_toggle = checkbox(
    name="default",
    text="Default Values",
    pos=scene.title_anchor,
    bind= loop_toggle,
    checked=True,
)
surface_toggle = checkbox(
    name="shape", text=" Unique Values     ", pos=scene.title_anchor, bind= surface_loop_toggle, checked = False 
)


       
  
def alteralpha(s): 
    currSlider.disabled = loop_toggle.checked 
 
    if currSlider.disabled: 
        s.value = 15.6
    else:
        alpha_beta[0] = s.value 
    wt1.text = '{:1.2f} alpha\n'.format(s.value) # f-string! to display the values 
    clear()

def alterbeta(a): 
    anotherSlider.disabled = loop_toggle.checked 
 
    if anotherSlider.disabled: 
        a.value = 28
    else:
        alpha_beta[1] = a.value 
    wt2.text = '{:1.2f} beta\n'.format(a.value) # f-string! to display the values 
    clear()

  

#slider to update the value of charge/current 

    


g1 = gdots(graph = g1_g) 
g2 = gdots(graph = g2_g)
g3 = gdots(graph = g3_g)
#
def conversion_function(x_hat):
    return m1 * x_hat + 0.5 * (m0 - m1)* (abs(x_hat + 1 ) - abs(x_hat - 1))
dt = 0.01

currSlider = slider(bind=alteralpha, min= 0.05, max=20.1,step=0.1, value = 15.6, length= 300 ,width=15, align = "left", pos=scene.caption_anchor, disabled = True )
wt1 = wtext(text='{:1.2f} alpha\n'.format(currSlider.value))  #dynamic text! 

anotherSlider = slider(bind=alterbeta, min= 0.05, max=30,step=0.1, value = 28, length= 300 ,width=15, align = "left", pos=scene.caption_anchor, disabled = True )
wt2 = wtext(text='{:1.2f} beta \n'.format(anotherSlider.value))
while True:
    rate(60)
    x_1 = fun_arr[0]
    y_1 = fun_arr[1]
    z_1 = fun_arr[2]
    alpha = alpha_beta[0]
    beta = alpha_beta[1]
    h = conversion_function(x_1)

    x_dot = alpha*(y_1 - x_1 - h)
    y_dot = x_1 - y_1 + z_1 
    z_dot  = -beta * y_1
    
    fun_arr[0] += x_dot * dt
    fun_arr[1] += y_dot * dt
    fun_arr[2] += z_dot * dt
    
    g1.plot(time_dt[0], x_1)
    g2.plot(time_dt[0], y_1)
    g3.plot(time_dt[0], z_1) 
    
    time_dt[0] += dt 
