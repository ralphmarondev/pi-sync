package com.ralphmarondev.pisync.features.privacy.data.network

import com.ralphmarondev.pisync.features.privacy.data.model.DoorListResponse
import com.ralphmarondev.pisync.features.privacy.data.model.ToggleAdminAccessResponse
import retrofit2.http.GET
import retrofit2.http.POST
import retrofit2.http.Path

interface PrivacyApiService {
    @GET("doors/username/{username}/")
    suspend fun getDoorsByUsername(@Path("username") username: String): DoorListResponse

    @POST("door/toggle-admin-access/{id}/")
    suspend fun toggleAdminAccess(@Path("id") doorId: Int): ToggleAdminAccessResponse
}
