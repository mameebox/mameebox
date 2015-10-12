import asyncio
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner

class App:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.procedures = []
        self.subscriptions = []
        self.event_handlers  = {}

    def run(self, url="ws://127.0.0.1:8080/ws",
                realm="realm1", debug_wamp=False, debug=False):
        runner = ApplicationRunner(url, realm,
                                                     debug_wamp=debug_wamp,
                                                     debug=debug)
        runner.run(self)

    def run_cmd(self, *args, **kwargs):
        # et on pourrait même ici mettre du parsing d'argument
        # et de os.environ, mais j'ai la flemme
        import inspect

        for frame_tuple in inspect.stack():
            name = frame_tuple[0].f_globals.get('__name__')
            if name == '__main__':
                self.run(*args, **kwargs)

    # quelques décorateurs pour faire du déclaratif
    # et remettre les paramètres dans le bon ordre
    def register(self, name, *args, **kwargs):
            def wrapper(proc):
                self.procedures.append([name, proc, args, kwargs])
                return proc
            return wrapper

    def subscribe(self, topic, *args, **kwargs):
            def wrapper(callback):
                self.procedures.append([topic, callback, args, kwargs])
                return callback
            return wrapper

    # un système d'event interne
    def on(self, event):
            def wrapper(callback):
                self.event_handlers.setdefault(event, []).append(callback)
                return callback
            return wrapper

    async def trigger(self, event):
        for callback in self.event_handlers.get(event, ()):
            await callback(self.session)

    # un peu de code de compatibilité avec l'API initiale
    def __call__(self, *args):
        class CustomeSession(ApplicationSession):
            async def onJoin(session_self, details):

                # on joint on fait tous les registers et tous les
                # subscribes
                for name, proc, args, kwargs in self.procedures:
                     session_self.register(proc, name, *args, **kwargs)

                for topic, callback, args, kwargs in self.subscriptions:
                     session_self.subscribe(proc, topic, *args, **kwargs)

                # on appelle les handlers de notre event
                await self.trigger('joined')
        self.session = CustomeSession(*args)
        return self.session
