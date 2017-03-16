class Target(object):
    def target_method(self):
        self.can_print = False
        self.validate()
        if self.can_print:
            return 'OK'
        return 'NG'

    def validate(self):
        is_ok = False

        # Complicated process...

        if is_ok:
            self.can_print = True