# Comment class
class Comment:
    comments = []
    current_id = 0

    def list(self):
        return Comment.comments

    def add(self, body):
        Comment.current_id += 1
        comment = {
            'id': Comment.current_id,
            'body': body
        }
        Comment.comments.append(comment)
        return comment

    def delete(self, comment_id):
        # check if user can delete
        for i, comment in enumerate(Comment.comments):
            if comment['id'] == comment_id:
                del Comment.comments[i]
        return True

# Reply class
