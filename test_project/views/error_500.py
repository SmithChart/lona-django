import traceback

from lona.default_views import Error500View as _Error500View


class Error500View(_Error500View):
    def handle_request(self, request, exception):
        if request.url.path == '/crashes/handle-500/':
            raise ValueError('Success! This should crash!')

        if not request.user.is_authenticated:
            return self.render_default_template(request, exception=exception)

        exception_string = ''.join(
            traceback.format_exception(
                etype=type(exception),
                value=exception,
                tb=exception.__traceback__,
            )
        )

        return """
            <h2>500</h2>
            <pre>{}</pre>
        """.format(
            exception_string,
        )
