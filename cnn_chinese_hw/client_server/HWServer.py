from speedysvc.service_method import service_method

from cnn_chinese_hw.client_server.rem_dupes import rem_dupes
from cnn_chinese_hw.recognizer.TFLiteRecognizer import TFLiteRecognizer


USE_ZINNIA = False


class HWServer:
    def __init__(self):
        self.recognizer = TFLiteRecognizer()

    @service_method()
    def get_cn_written_cand(self, LStrokes, id):
        if not LStrokes:
            # TODO: Also handle single stroke candidates differently!
            return {'LCands': [], 'id': id}

        return_list = [
            chr(ord_) for _, ord_ in
            self.recognizer.get_L_candidates(LStrokes)
        ]

        return_list = rem_dupes(return_list)
        return_dict = {'LCands': return_list, 'id': id}
        return return_dict
