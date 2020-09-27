#watchdog_example

import watchdog.events
import watchdog.observers
import shutil

#The handler class
class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.txt', '*.png', '*.jpg'], ignore_patterns = None,
                                                     ignore_directories = False, case_sensitive = True)

    def on_created(self, event):
        print(f"File was created at {event.src_path}")
        if event.src_path.endswith('.txt'): 
            shutil.move(event.src_path, r'C:\Users\win10\Desktop\Text_Documents')           #You may have to change the path
        elif event.src_path.endswith('.png') or event.src_path.endswith('.jpg'): 
            shutil.move(event.src_path, r'C:\Users\win10\Desktop\Image_docs')               #You may have to change the path
    def on_deleted(self, event):
        print(f"File was deleted at {event.src_path}")


event_handler = Handler()
observer = watchdog.observers.Observer()
observer.schedule(event_handler, r'C:\Users\win10\Desktop', recursive = False)
observer.start()
observer.join()

        

    
        
        
