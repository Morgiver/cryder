
import Windows


class WindowsBuilder:
    @staticmethod
    def build(app_instance, class_name, **kwargs):
        window_class = getattr(Windows, class_name)
        w = window_class(app_instance)

        for key in kwargs:
            try:
                m = getattr(w, key)
                m(kwargs[key])
            except:
                pass

        return w