package com.ralphmarondev.pisync.features.auth.presentation

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.ralphmarondev.pisync.core.model.LoginRequest
import com.ralphmarondev.pisync.features.auth.data.repository.AuthRepositoryImpl
import com.ralphmarondev.pisync.features.auth.domain.usecases.LoginUseCase
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch

class AuthViewModel : ViewModel() {
    private val repository = AuthRepositoryImpl()
    private val loginUseCase = LoginUseCase(repository)

    private val _username = MutableStateFlow("")
    val username: StateFlow<String> get() = _username

    private val _password = MutableStateFlow("")
    val password: StateFlow<String> get() = _password

    fun onUsernameChange(value: String) {
        _username.value = value
    }

    fun onPasswordChange(value: String) {
        _password.value = value
    }

    fun login(
        response: (Boolean, String?) -> Unit
    ) {
        viewModelScope.launch {
            val loginRequest = LoginRequest(_username.value.trim(), _password.value.trim())
            loginUseCase.login(loginRequest, response)
        }
    }
}