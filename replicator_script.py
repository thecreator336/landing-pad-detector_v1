import omni.replicator.core as rep
import time

with rep.new_layer():

    camera = rep.create.camera(position=(0, 0, 3200), look_at=(0, 0, 0))
    render_product = rep.create.render_product(camera, resolution=(640, 480))

    landing_pad = rep.get.prims("/World/LandingPad")
    with landing_pad:
        rep.modify.semantics([("class", "landing_pad")])

    writer = rep.WriterRegistry.get("BasicWriter")
    writer.initialize(
        output_dir="C:/landing_dataset",
        rgb=True,
        bounding_box_2d_tight=True,
    )
    writer.attach([render_product])

    with rep.trigger.on_frame(num_frames=100, rt_subframes=8):
        with camera:
            rep.modify.pose(
                position=rep.distribution.uniform(
                    (-8000, -8000, 2800),
                    (8000, 8000, 8800)
                ),
                look_at=(0, 0, 0)
            )

        sun_light = rep.get.light(path_pattern="SunLight")
        with sun_light:
            rep.modify.attribute("intensity", rep.distribution.uniform(500.0, 8000.0))
            rep.modify.pose(
                rotation=rep.distribution.uniform(
                    (-60, 0, 0),
                    (-30, 360, 0)
                )
            )

        dome_light = rep.get.light(path_pattern="DomeLight")
        with dome_light:
            rep.modify.attribute("intensity", rep.distribution.uniform(200.0, 800.0))

rep.orchestrator.preview()
writer.attach([render_product])
rep.orchestrator.run()

time.sleep(60)
print("Done — check C:/landing_dataset")
