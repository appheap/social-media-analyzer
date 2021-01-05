from db.scaffold import Scaffold


class AdminLogExists(Scaffold):
    def admin_log_exists(
            self,
            *,
            event_id: int,
            chat_id: int,
    ) -> bool:
        return self.tg_models.AdminLogEvent.objects.admin_log_exists(
            event_id=event_id,
            chat_id=chat_id,
        )
