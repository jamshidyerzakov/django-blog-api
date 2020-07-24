from typing import Dict


def validate_data(**data) -> Dict:
    validated_data = {}
    try:
        if data.get('commenter_id', None) and isinstance(data.get('commenter_id', None), int):
            validated_data['commenter_id'] = data['commenter_id']
        if data.get('post_id', None) and isinstance(data.get('post_id', None), int):
            validated_data['post_id'] = data['post_id']
        if data.get('reply_to_id', None) and isinstance(data.get('reply_to_id', None), int):
            validated_data['reply_to_id'] = data['reply_to_id']
        if data.get('content', None) and isinstance(data.get('content', None), str):
            validated_data['content'] = data['content']

        return validated_data
    except KeyError:
        return {"error": "Validation error"}