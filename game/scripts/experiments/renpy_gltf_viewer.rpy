default citydom_gltf_preview_rot_y = 0.0
default citydom_gltf_preview_zoom = 115.0

init python:
    renpy.register_shader("citydom.gltf_preview", variables="""
        uniform mat4 u_model__inverse_transpose;
        uniform vec4 u_color_diffuse;
        uniform vec4 u_color_specular;
        uniform sampler2D u_tex_diffuse;

        varying vec3 v_normal;
        varying vec2 v_tex_coord;

        attribute vec3 a_normal;
        attribute vec2 a_tex_coord;
    """, vertex_201="""
        v_normal = (u_model__inverse_transpose * vec4(a_normal, 1.0)).xyz;
        v_tex_coord = a_tex_coord;
    """, fragment_201="""
        vec3 normal = normalize(v_normal);
        vec3 lightDir = normalize(vec3(-0.25, -0.65, 1.0));
        float lambertian = max(dot(normal, lightDir), 0.0);
        float wrapped = max(lambertian * 0.65 + 0.35, 0.0);

        vec4 diffuse = texture2D(u_tex_diffuse, v_tex_coord.xy);
        vec3 base = diffuse.rgb * max(u_color_diffuse.rgb, vec3(0.001));

        vec3 viewDir = normalize(vec3(0.0, 0.0, -1.0));
        vec3 halfDir = normalize(lightDir + viewDir);
        float specular = pow(max(dot(normal, halfDir), 0.0), 24.0);
        vec3 spec = u_color_specular.rgb * u_color_specular.a * specular * 0.20;

        gl_FragColor = vec4(base * wrapped + spec, diffuse.a * u_color_diffuse.a);
        if (gl_FragColor.a < 0.45) {
            discard;
        }
    """)

    def citydom_gltf_available(name):
        return name == "Maria" and renpy.loadable("assets_3d/characters/maria/maria_probe.glb")

    def citydom_gltf_adjust_rotation(delta):
        store.citydom_gltf_preview_rot_y = (store.citydom_gltf_preview_rot_y + delta) % 360.0
        renpy.restart_interaction()

    def citydom_gltf_adjust_zoom(delta):
        store.citydom_gltf_preview_zoom = max(35.0, min(260.0, store.citydom_gltf_preview_zoom + delta))
        renpy.restart_interaction()

screen citydom_gltf_character_preview():
    key "mousedown_4" action Function(citydom_gltf_adjust_zoom, 6.0)
    key "mousedown_5" action Function(citydom_gltf_adjust_zoom, -6.0)

    fixed:
        xysize (430, 520)
        add GLTFModel(
            "assets_3d/characters/maria/maria_probe.glb",
            shader="citydom.gltf_preview",
            zoom=citydom_gltf_preview_zoom,
            report=False,
        ):
            xpos 215
            ypos 500
            xanchor 0.5
            yanchor 1.0
            xrotate -8.0
            yrotate citydom_gltf_preview_rot_y
            gl_depth True

    hbox:
        xpos 58
        ypos 524
        spacing 8
        textbutton "ROT -" action Function(citydom_gltf_adjust_rotation, -12.0):
            style "citydom_details_micro_button"
        textbutton "ROT +" action Function(citydom_gltf_adjust_rotation, 12.0):
            style "citydom_details_micro_button"
        textbutton "ZOOM -" action Function(citydom_gltf_adjust_zoom, -8.0):
            style "citydom_details_micro_button"
        textbutton "ZOOM +" action Function(citydom_gltf_adjust_zoom, 8.0):
            style "citydom_details_micro_button"

style citydom_details_micro_button is default:
    background Solid("#16001fb8")
    hover_background Solid("#421653cc")
    padding (8, 4)
    font "fonts/citydom_ui/SpaceGrotesk-Medium.ttf"
    size 10
    color "#e9b8ff"
