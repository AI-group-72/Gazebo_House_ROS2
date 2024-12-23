1. Есть ли у робота камера и лидар? У меня да! (кажется...)

Файл робота: file:///home/taisia/ros2_ws_1/src/turtlebot3_simulations/turtlebot3_gazebo/models/turtlebot3_waffle/model.sdf

У вас путь, конечно же, может отличаться)

```
<?xml version="1.0" ?>
<sdf version="1.5">
  <model name="turtlebot3_waffle">  
  <pose>0.0 0.0 0.0 0.0 0.0 0.0</pose>

    <link name="base_footprint"/>

    <link name="base_link">

      <inertial>
        <pose>-0.064 0 0.048 0 0 0</pose>
        <inertia>
          <ixx>4.2111447e-02</ixx>
          <ixy>0</ixy>
          <ixz>0</ixz>
          <iyy>4.2111447e-02</iyy>
          <iyz>0</iyz>
          <izz>7.5254874e-02</izz>
        </inertia>
        <mass>1.3729096e+00</mass>
      </inertial>

      <collision name="base_collision">
        <pose>-0.064 0 0.048 0 0 0</pose>
        <geometry>
          <box>
            <size>0.265 0.265 0.089</size>
          </box>
        </geometry>
      </collision>

      <visual name="base_visual">
        <pose>-0.064 0 0 0 0 0</pose>
        <geometry>
          <mesh>
            <uri>model://turtlebot3_common/meshes/waffle_base.dae</uri>
            <scale>0.001 0.001 0.001</scale>
          </mesh>
        </geometry>
      </visual>
    </link>

    <link name="imu_link">
      <sensor name="tb3_imu" type="imu">
        <always_on>true</always_on>
        <update_rate>200</update_rate>
        <imu>
          <angular_velocity>
            <x>
              <noise type="gaussian">
                <mean>0.0</mean>
                <stddev>2e-4</stddev>
              </noise>
            </x>
            <y>
              <noise type="gaussian">
                <mean>0.0</mean>
                <stddev>2e-4</stddev>
              </noise>
            </y>
            <z>
              <noise type="gaussian">
                <mean>0.0</mean>
                <stddev>2e-4</stddev>
              </noise>
            </z>
          </angular_velocity>
          <linear_acceleration>
            <x>
              <noise type="gaussian">
                <mean>0.0</mean>
                <stddev>1.7e-2</stddev>
              </noise>
            </x>
            <y>
              <noise type="gaussian">
                <mean>0.0</mean>
                <stddev>1.7e-2</stddev>
              </noise>
            </y>
            <z>
              <noise type="gaussian">
                <mean>0.0</mean>
                <stddev>1.7e-2</stddev>
              </noise>
            </z>
          </linear_acceleration>
        </imu>
        <plugin name="turtlebot3_imu" filename="libgazebo_ros_imu_sensor.so">
          <ros>
            <!-- <namespace>/tb3</namespace> -->
            <remapping>~/out:=imu</remapping>
          </ros>
        </plugin>
      </sensor>
    </link>

    <link name="base_scan">    
      <inertial>
        <pose>-0.052 0 0.111 0 0 0</pose>
        <inertia>
          <ixx>0.001</ixx>
          <ixy>0.000</ixy>
          <ixz>0.000</ixz>
          <iyy>0.001</iyy>
          <iyz>0.000</iyz>
          <izz>0.001</izz>
        </inertia>
        <mass>0.114</mass>
      </inertial>

      <collision name="lidar_sensor_collision">
        <pose>-0.052 0 0.111 0 0 0</pose>
        <geometry>
          <cylinder>
            <radius>0.0508</radius>
            <length>0.055</length>
          </cylinder>
        </geometry>
      </collision>

      <visual name="lidar_sensor_visual">
        <pose>-0.064 0 0.121 0 0 0</pose>
        <geometry>
          <mesh>
            <uri>model://turtlebot3_common/meshes/lds.dae</uri>
            <scale>0.001 0.001 0.001</scale>
          </mesh>
        </geometry>
      </visual>

      <sensor name="hls_lfcd_lds" type="ray">
        <always_on>true</always_on>
        <visualize>true</visualize>
        <pose>-0.064 0 0.121 0 0 0</pose>
        <update_rate>5</update_rate>
        <ray>
          <scan>
            <horizontal>
              <samples>360</samples>
              <resolution>1.000000</resolution>
              <min_angle>0.000000</min_angle>
              <max_angle>6.280000</max_angle>
            </horizontal>
          </scan>
          <range>
            <min>0.120000</min>
            <max>3.5</max>
            <resolution>0.015000</resolution>
          </range>
          <noise>
            <type>gaussian</type>
            <mean>0.0</mean>
            <stddev>0.01</stddev>
          </noise>
        </ray>
        <plugin name="turtlebot3_laserscan" filename="libgazebo_ros_ray_sensor.so">
          <ros>
            <!-- <namespace>/tb3</namespace> -->
            <remapping>~/out:=scan</remapping>
          </ros>
          <output_type>sensor_msgs/LaserScan</output_type>
          <frame_name>base_scan</frame_name>
        </plugin>
      </sensor>
    </link>

    <link name="wheel_left_link">

      <inertial>
        <pose>0.0 0.144 0.023 -1.57 0 0</pose>
        <inertia>
          <ixx>1.1175580e-05</ixx>
          <ixy>-4.2369783e-11</ixy>
          <ixz>-5.9381719e-09</ixz>
          <iyy>1.1192413e-05</iyy>
          <iyz>-1.4400107e-11</iyz>
          <izz>2.0712558e-05</izz>
        </inertia>
        <mass>0.1</mass>
      </inertial>

      <collision name="wheel_left_collision">
        <pose>0.0 0.144 0.023 -1.57 0 0</pose>
        <geometry>
          <cylinder>
            <radius>0.033</radius>
            <length>0.018</length>
          </cylinder>
        </geometry>
        <surface>
          <!-- This friction pamareter don't contain reliable data!! -->
          <friction>
            <ode>
              <mu>100000.0</mu>
              <mu2>100000.0</mu2>
              <fdir1>0 0 0</fdir1>
              <slip1>0.0</slip1>
              <slip2>0.0</slip2>
            </ode>
          </friction>
          <contact>
            <ode>
              <soft_cfm>0</soft_cfm>
              <soft_erp>0.2</soft_erp>
              <kp>1e+5</kp>
              <kd>1</kd>
              <max_vel>0.01</max_vel>
              <min_depth>0.001</min_depth>
            </ode>
          </contact>
        </surface>
      </collision>

      <visual name="wheel_left_visual">
        <pose>0.0 0.144 0.023 0 0 0</pose>
        <geometry>
          <mesh>
            <uri>model://turtlebot3_common/meshes/tire.dae</uri>
            <scale>0.001 0.001 0.001</scale>
          </mesh>
        </geometry>
      </visual>
    </link>

    <link name="wheel_right_link">

      <inertial>
        <pose>0.0 -0.144 0.023 -1.57 0 0</pose>
        <inertia>
          <ixx>1.1175580e-05</ixx>
          <ixy>-4.2369783e-11</ixy>
          <ixz>-5.9381719e-09</ixz>
          <iyy>1.1192413e-05</iyy>
          <iyz>-1.4400107e-11</iyz>
          <izz>2.0712558e-05</izz>
        </inertia>
        <mass>0.1</mass>
      </inertial>
    
      <collision name="wheel_right_collision">
        <pose>0.0 -0.144 0.023 -1.57 0 0</pose>
        <geometry>
          <cylinder>
            <radius>0.033</radius>
            <length>0.018</length>
          </cylinder>
        </geometry>
        <surface>
          <!-- This friction pamareter don't contain reliable data!! -->
          <friction>
            <ode>
              <mu>100000.0</mu>
              <mu2>100000.0</mu2>
              <fdir1>0 0 0</fdir1>
              <slip1>0.0</slip1>
              <slip2>0.0</slip2>
            </ode>
          </friction>
          <contact>
            <ode>
              <soft_cfm>0</soft_cfm>
              <soft_erp>0.2</soft_erp>
              <kp>1e+5</kp>
              <kd>1</kd>
              <max_vel>0.01</max_vel>
              <min_depth>0.001</min_depth>
            </ode>
          </contact>
        </surface>
      </collision>

      <visual name="wheel_right_visual">
        <pose>0.0 -0.144 0.023 0 0 0</pose>
        <geometry>
          <mesh>
            <uri>model://turtlebot3_common/meshes/tire.dae</uri>
            <scale>0.001 0.001 0.001</scale>
          </mesh>
        </geometry>
      </visual>
    </link>

    <link name='caster_back_right_link'>
      <pose>-0.177 -0.064 -0.004 -1.57 0 0</pose>
      <inertial>
        <mass>0.001</mass>
        <inertia>
          <ixx>0.00001</ixx>
          <ixy>0.000</ixy>
          <ixz>0.000</ixz>
          <iyy>0.00001</iyy>
          <iyz>0.000</iyz>
          <izz>0.00001</izz>
        </inertia>
      </inertial>
      <collision name='collision'>
        <geometry>
          <sphere>
            <radius>0.005000</radius>
          </sphere>
        </geometry>
        <surface>
          <contact>
            <ode>
              <soft_cfm>0</soft_cfm>
              <soft_erp>0.2</soft_erp>
              <kp>1e+5</kp>
              <kd>1</kd>
              <max_vel>0.01</max_vel>
              <min_depth>0.001</min_depth>
            </ode>
          </contact>
        </surface>
      </collision>
    </link>

    <link name='caster_back_left_link'>
      <pose>-0.177 0.064 -0.004 -1.57 0 0</pose>
      <inertial>
        <mass>0.001</mass>
        <inertia>
          <ixx>0.00001</ixx>
          <ixy>0.000</ixy>
          <ixz>0.000</ixz>
          <iyy>0.00001</iyy>
          <iyz>0.000</iyz>
          <izz>0.00001</izz>
        </inertia>
      </inertial>
      <collision name='collision'>
        <geometry>
          <sphere>
            <radius>0.005000</radius>
          </sphere>
        </geometry>
        <surface>
          <contact>
            <ode>
              <soft_cfm>0</soft_cfm>
              <soft_erp>0.2</soft_erp>
              <kp>1e+5</kp>
              <kd>1</kd>
              <max_vel>0.01</max_vel>
              <min_depth>0.001</min_depth>
            </ode>
          </contact>
        </surface>
      </collision>
    </link>

    <link name="camera_link"/>

    <link name="camera_rgb_frame">
      <inertial>
        <pose>0.069 -0.047 0.107 0 0 0</pose>
        <inertia>
          <ixx>0.001</ixx>
          <ixy>0.000</ixy>
          <ixz>0.000</ixz>
          <iyy>0.001</iyy>
          <iyz>0.000</iyz>
          <izz>0.001</izz>
        </inertia>
        <mass>0.035</mass>
      </inertial>

      <pose>0.069 -0.047 0.107 0 0 0</pose>
      <sensor name="camera" type="camera">
        <always_on>true</always_on>
        <visualize>true</visualize>
        <update_rate>30</update_rate>
        <camera name="intel_realsense_r200">
          <horizontal_fov>1.02974</horizontal_fov>
          <image>
            <width>1920</width>
            <height>1080</height>
            <format>R8G8B8</format>
          </image>
          <clip>
            <near>0.02</near>
            <far>300</far>
          </clip>
          <noise>
            <type>gaussian</type>
            <!-- Noise is sampled independently per pixel on each frame.
                  That pixel's noise value is added to each of its color
                  channels, which at that point lie in the range [0,1]. -->
            <mean>0.0</mean>
            <stddev>0.007</stddev>
          </noise>
        </camera>
          <plugin name="camera_driver" filename="libgazebo_ros_camera.so">
            <always_on>true</always_on>
            <update_rate>30</update_rate>
            <camera_name>camera</camera_name>
            <image_topic_name>camera/image_raw</image_topic_name>
            <camera_info_topic_name>camera/camera_info</camera_info_topic_name>
            <frame_name>camera_rgb_frame</frame_name>
          </plugin>
      </sensor>
    </link>    

    <joint name="base_joint" type="fixed">
      <parent>base_footprint</parent>
      <child>base_link</child>
      <pose>0.0 0.0 0.010 0 0 0</pose>
    </joint>

    <joint name="wheel_left_joint" type="revolute">
      <parent>base_link</parent>
      <child>wheel_left_link</child>
      <pose>0.0 0.144 0.023 -1.57 0 0</pose>
      <axis>
        <xyz>0 0 1</xyz>
      </axis>
    </joint>

    <joint name="wheel_right_joint" type="revolute">
      <parent>base_link</parent>
      <child>wheel_right_link</child>
      <pose>0.0 -0.144 0.023 -1.57 0 0</pose>
      <axis>
        <xyz>0 0 1</xyz>
      </axis>
    </joint>

    <joint name='caster_back_right_joint' type='ball'>
      <parent>base_link</parent>
      <child>caster_back_right_link</child>
    </joint>

    <joint name='caster_back_left_joint' type='ball'>
      <parent>base_link</parent>
      <child>caster_back_left_link</child>
    </joint>

    <joint name="imu_joint" type="fixed">
      <parent>base_link</parent>
      <child>imu_link</child>
      <pose>-0.032 0 0.068 0 0 0</pose>
      <axis>
        <xyz>0 0 1</xyz>
      </axis>
    </joint>    

    <joint name="lidar_joint" type="fixed">
      <parent>base_link</parent>
      <child>base_scan</child>
      <pose>-0.064 0 0.121 0 0 0</pose>
      <axis>
        <xyz>0 0 1</xyz>
      </axis>
    </joint>

    <joint name="camera_joint" type="fixed">
      <parent>base_link</parent>
      <child>camera_link</child>
      <pose>0.064 -0.065 0.094 0 0 0</pose>
      <axis>
        <xyz>0 0 1</xyz>
      </axis>
    </joint>

    <joint name="camera_rgb_joint" type="fixed">
      <parent>camera_link</parent>
      <child>camera_rgb_frame</child>
      <pose>0.005 0.018 0.013 0 0 0</pose>
      <axis>
        <xyz>0 0 1</xyz>
      </axis>
    </joint>

    <plugin name="turtlebot3_diff_drive" filename="libgazebo_ros_diff_drive.so">

      <ros>
        <!-- <namespace>/tb3</namespace> -->
      </ros>

      <update_rate>30</update_rate>

      <!-- wheels -->
      <left_joint>wheel_left_joint</left_joint>
      <right_joint>wheel_right_joint</right_joint>

      <!-- kinematics -->
      <wheel_separation>0.287</wheel_separation>
      <wheel_diameter>0.066</wheel_diameter>

      <!-- limits -->
      <max_wheel_torque>20</max_wheel_torque>
      <max_wheel_acceleration>1.0</max_wheel_acceleration>

      <command_topic>cmd_vel</command_topic>

      <!-- output -->
      <publish_odom>true</publish_odom>
      <publish_odom_tf>true</publish_odom_tf>
      <publish_wheel_tf>false</publish_wheel_tf>

      <odometry_topic>odom</odometry_topic>
      <odometry_frame>odom</odometry_frame>
      <robot_base_frame>base_footprint</robot_base_frame>

    </plugin>

    <plugin name="turtlebot3_joint_state" filename="libgazebo_ros_joint_state_publisher.so">
      <ros>
        <!-- <namespace>/tb3</namespace> -->
        <remapping>~/out:=joint_states</remapping>
      </ros>
      <update_rate>30</update_rate>
      <joint_name>wheel_left_joint</joint_name>
      <joint_name>wheel_right_joint</joint_name>
    </plugin>    

  </model>
</sdf>
```

2. Запускаем робота в мире:

```
taisia@taisia-Inspiron-5558:~$ source /opt/ros/humble/setup.bash
taisia@taisia-Inspiron-5558:~$ cd ros2_ws_1
taisia@taisia-Inspiron-5558:~/ros2_ws_1$ source ~/ros2_ws_1/install/setup.bash
taisia@taisia-Inspiron-5558:~/ros2_ws_1$ export TURTLEBOT3_MODEL=waffle
ros2 launch turtlebot3_gazebo world_smaller.launch.py
```

3. Топик скана

```
taisia@taisia-Inspiron-5558:~/ros2_ws_1$ source /opt/ros/humble/setup.bash
taisia@taisia-Inspiron-5558:~/ros2_ws_1$ source ~/ros2_ws_1/install/setup.bash
taisia@taisia-Inspiron-5558:~/ros2_ws_1$ export TURTLEBOT3_MODEL=waffle
taisia@taisia-Inspiron-5558:~/ros2_ws_1$ ros2 topic list
taisia@taisia-Inspiron-5558:~/ros2_ws_1$ ros2 topic echo /scan
```

4. Скачать и запустить слэм:

В новом терминале

```
taisia@taisia-Inspiron-5558:~/ros2_ws_1$ source /opt/ros/humble/setup.bash
taisia@taisia-Inspiron-5558:~/ros2_ws_1$ source ~/ros2_ws_1/install/setup.bash
```

- Установка:
```
sudo apt install ros-humble-slam-toolbox
```
- Запуск:

```
export TURTLEBOT3_MODEL=waffle
ros2 launch slam_toolbox online_async_launch.py
```

5. Визуализация:

```
source /opt/ros/humble/setup.bash
source ~/ros2_ws_1/install/setup.bash
ros2 run rviz2 rviz2
```

В RViz:

- Найдите кнопку "Add" в левой панели.
- Выберите "Map" и подключите его к топику /map. Карта должна начать отображаться.
- Добавьте дисплей "LaserScan":
- Также через кнопку "Add" выберите "LaserScan".
- Подключите его к топику /scan. Вы должны увидеть данные лидара в виде точек.

Там же добавляем топик камеры
```
/camera/image_raw
```

Если бы мы не строили карту, то чисто для визуализации можно
```
ros2 run rqt_image_view rqt_image_view
```

В окошечке, которое появляется выбираем топик камеры (например, /camera/image_raw)

6. Управление:

```
source /opt/ros/humble/setup.bash
source ~/ros2_ws_1/install/setup.bash
ros2 run turtlebot3_teleop teleop_keyboard
```


Двигаем робота. рисуем карту, когда доделали, жмакаем в новом терминале:

```
source /opt/ros/humble/setup.bash
source ~/ros2_ws_1/install/setup.bash
ros2 run nav2_map_server map_saver_cli -f ~/ros2_ws_1/map
```

Отлично, у нас уже есть карта по итогу этого скрипта!

Карта сохранится в файлы map.yaml и map.pgm (или .png) в директории ~/ros2_ws_1

Имейте в виде, если переделываете карту, пишите map2, например, в конце. Иначе перезапишется картинка, и старая удалится!


7. Далее (а можно и параллельно с предыдущим шагом):

Запускаем в новом терминале скрипты. Скрипты мы кладём в рабочую директорию в папку scripts: ~/ros2_ws_1/scripts

```
python3 run_all_scripts.py
```

Что делают скрипты:

- Каждый скрипт может работать по отдельности, но если хочется запустить сразу, то это run_all_scripts.py
- Скрипты создают фотографии с камеры робота, и снимают данные с лидара. Фото записываются в папку images.
- Всё это объединяется в csv файл, где есть время создания строки, путь до изображения, соответствующие данные с лидара.
- Три разных скрипта создают три разные варианта чтения картинки: шифровка в RGB, шифровка в bytesIO, и просто запись пути до изображения: "images/image_20241215_152156.png"
