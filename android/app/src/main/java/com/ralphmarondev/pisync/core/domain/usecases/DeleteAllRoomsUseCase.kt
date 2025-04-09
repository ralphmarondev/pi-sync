package com.ralphmarondev.pisync.core.domain.usecases

import com.ralphmarondev.pisync.core.domain.repositories.RoomRepository

class DeleteAllRoomsUseCase(
    private val repository: RoomRepository
) {
    suspend operator fun invoke() {
        repository.deleteAllRooms()
    }
}