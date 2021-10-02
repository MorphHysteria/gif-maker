from cv2 import VideoCapture, CAP_PROP_FRAME_COUNT, CAP_PROP_FPS, cvtColor, COLOR_BGR2RGB
from imageio import mimsave

resource_path = "Pruebas/Prueba_1.mkv"
cap = VideoCapture(resource_path)
frames = cap.get(CAP_PROP_FRAME_COUNT)
print(f"Frames {frames}")
fps = cap.get(CAP_PROP_FPS)
print(f"FPS: {fps}")

x = input("Start process? (y/n): ")
if x.lower() == 'n':
    print("Exit program.")
    exit(0)
elif x.lower() == 'y':
    actual_frame = 0
    GIF_Frames = []
    initial_frame = 1060
    final_frame = 1471
    gif_fps = 24

    print("Searching initial frame...")
    while True:
        ret, frame = cap.read()
        if not ret: break
        actual_frame += 1
        if (actual_frame >= initial_frame) and (actual_frame <= final_frame):
            if actual_frame == initial_frame: print("Collecting frames...")
            if actual_frame == final_frame: print("Done!")
            GIF_Frames.append(cvtColor(frame, COLOR_BGR2RGB))
    cap.release()

    if (final_frame - initial_frame + 1) != len(GIF_Frames): print("Error while saving GIF!")
    else:
        # Save GIF file
        print("Saving GIF file...")
        mimsave("saved_GIF.gif", GIF_Frames, fps=gif_fps)
        print("Saved!")