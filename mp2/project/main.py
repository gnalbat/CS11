import engine
from engine import pyglet, config, import_module, path, datetime, mkdir

def initialize():
    engine.get_images()

    img = []
    sprite = []

    template = config['template']
    template_config_path = 'resources/templates/' + template + '/'

    path.append(template_config_path)

    template_config = import_module(template, package=None)

    frame = pyglet.image.load('resources/templates/' + template + '/frame.png')
    frame_sprite = pyglet.sprite.Sprite(frame)

    for i in range(4):
        img.append(pyglet.image.load('tmp/photo_' + '{}'.format(i) + '.png'))

    for i in range(4):
        sprite.append(pyglet.sprite.Sprite(img[int('{}'.format(i))]))

    sprite[0].scale = (frame.width/img[0].width) * template_config.config['scale0']
    sprite[1].scale = (frame.width/img[1].width) * template_config.config['scale1']
    sprite[2].scale = (frame.width/img[2].width) * template_config.config['scale2']
    sprite[3].scale = (frame.width/img[3].width) * template_config.config['scale3']

    sprite[0].position = template_config.config['pos0']
    sprite[1].position = template_config.config['pos1']
    sprite[2].position = template_config.config['pos2']
    sprite[3].position = template_config.config['pos3']

    return frame, frame_sprite, sprite

class OutputWindow(pyglet.window.Window):
    def on_draw(self):
        self.clear()
        sprite[1].draw()
        sprite[2].draw()
        sprite[3].draw()
        sprite[0].draw()
        frame_sprite.draw()
    
        try:
            mkdir('output')
        except FileExistsError:
            pass
        
        now = datetime.datetime.now()
        timestamp = (now.year, now.month, now.day, '_', now.hour, now.minute, now.second)
        timestamp = [str(i) for i in timestamp]

        for i in range(len(timestamp)):
            if len(timestamp[i]) < 2 and (timestamp[i] != '_'):
                timestamp[i] = '0' + timestamp[i]

        pyglet.image.get_buffer_manager().get_color_buffer().save('output/output_{}.png'.format(''.join(timestamp)))

    def exit_callback(self):
        self.close()

if __name__ == "__main__":
    frame, frame_sprite, sprite = initialize()
    output_window = OutputWindow(width=frame.width, height=frame.height, caption='Output')
    pyglet.clock.schedule_once(OutputWindow.exit_callback, int('{}'.format(config['timeout']))) 
    pyglet.app.run()
