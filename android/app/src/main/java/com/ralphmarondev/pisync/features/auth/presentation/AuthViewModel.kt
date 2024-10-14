package com.ralphmarondev.pisync.features.auth.presentation

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.ralphmarondev.pisync.core.model.LoginRequest
import com.ralphmarondev.pisync.features.auth.data.repository.AuthRepositoryImpl
import com.ralphmarondev.pisync.features.auth.domain.usecases.LoginUseCase
import kotlinx.coroutines.launch

class AuthViewModel : ViewModel() {
    private val repository = AuthRepositoryImpl()
    private val loginUseCase = LoginUseCase(repository)

    fun login(
        username: String,
        password: String,
        response: (Boolean, String?) -> Unit
    ) {
        viewModelScope.launch {
            val loginRequest = LoginRequest(username, password)
            loginUseCase.login(loginRequest, response)
        }
    }
}