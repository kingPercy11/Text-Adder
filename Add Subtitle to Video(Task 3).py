import cv2


def add_subtitles(input_video_path, subtitle_text, output_video_path=None, position=(50, 50), font_size=1,font_color=(0, 0, 0)):
    video_capture = cv2.VideoCapture(input_video_path)
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    frame_width = int(video_capture.get(3))
    frame_height = int(video_capture.get(4))
    if not output_video_path:
        output_video_path = '/Users/pranjal/Desktop/SR DTU/Kingsgenius.mp4'
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height), isColor=True)
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        cv2.putText(frame, subtitle_text, tuple(position), cv2.FONT_HERSHEY_SIMPLEX, font_size, font_color, 2)
        video_writer.write(frame)
        cv2.imshow('Video with Subtitles', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    video_writer.release()
    cv2.destroyAllWindows()


input_video_path = input("Enter the path of the input video: ")
subtitle_text = input("Enter the subtitle text: ")
customize_position = input("Do you want to customize subtitle position? (y/n): ").lower() == 'y'
subtitle_position = tuple(
    map(int, input("Enter the subtitle position (x, y): ").split(','))) if customize_position else (50, 50)
customize_size = input("Do you want to customize subtitle font size? (y/n): ").lower() == 'y'
subtitle_font_size = float(input("Enter the subtitle font size (default is 1): ") or 1) if customize_size else 1
customize_color = input("Do you want to customize subtitle font color? (y/n): ").lower() == 'y'
subtitle_font_color = tuple(map(int, input("Enter the subtitle font color (R, G, B): ").split(','))) if customize_color else (255, 0, 0)
add_subtitles(input_video_path, subtitle_text, position=subtitle_position, font_size=subtitle_font_size, font_color=subtitle_font_color)
