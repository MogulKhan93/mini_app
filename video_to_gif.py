import ffmpeg
import os


def video_to_gif():
    # stream = ffmpeg.input('video/video_1.flv')
    # stream = ffmpeg.filter(stream, 'fps', fps=10)  # set the parameters of the source file here
    # stream = ffmpeg.output(stream, 'video_1.gif')
    # ffmpeg.run(stream)

    for file in os.listdir('video'):
        if file.endswith(('.mp4', '.MP4')):
            file_name = file.split('.')[0]
            gif_file = file_name + '.gif'

            stream = ffmpeg.input(f'video/{file}')
            stream = ffmpeg.filter(stream, 'fps', fps=5)
            stream = ffmpeg.output(stream, f'{gif_file}')
            ffmpeg.run(stream)


def main():
    video_to_gif()


if __name__ == '__main__':
    main()

