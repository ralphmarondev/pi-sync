package com.ralphmarondev.pisync.core.domain.usecases

import com.ralphmarondev.pisync.core.domain.model.Room
import com.ralphmarondev.pisync.core.domain.repositories.RoomRepository

class SaveRoomUseCase(
    private val repository: RoomRepository
) {
    suspend operator fun invoke(room: Room) {
        repository.saveRoom(room)
    }
}