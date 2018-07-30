class Reply:
    replies = []
    current_id = 0

    def add(self, comment_id, body):
        """
        Add a comment reply
        """
        # increment the id - for uniqueness
        Reply.current_id += 1
        # create reply
        reply = {
            'id': Reply.current_id,
            'comment_id': comment_id,
            'body': body
        }
        # append reply to list of replies
        Reply.replies.append(reply)
        # return the reply
        return reply
