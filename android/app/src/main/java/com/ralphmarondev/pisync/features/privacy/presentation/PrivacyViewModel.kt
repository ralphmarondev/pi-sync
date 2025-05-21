import android.util.Log
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.ralphmarondev.pisync.core.data.local.preferences.AppPreferences
import com.ralphmarondev.pisync.features.privacy.data.network.PrivacyApiService
import com.ralphmarondev.pisync.features.privacy.domain.model.Door
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

class PrivacyViewModel(
    private val api: PrivacyApiService,
    private val preferences: AppPreferences
) : ViewModel() {

    private val _doors = MutableStateFlow<List<Door>>(emptyList())
    val doors: StateFlow<List<Door>> = _doors

    private val _isLoading = MutableStateFlow(false)
    val isLoading: StateFlow<Boolean> = _isLoading

    private val _errorMessage = MutableStateFlow<String?>(null)
    val errorMessage: StateFlow<String?> = _errorMessage

    init {
        loadDoors(preferences.getCurrentUser() ?: "No username")
    }

    private fun loadDoors(username: String) {
        viewModelScope.launch {
            _isLoading.value = true
            _errorMessage.value = null
            try {
                val response = api.getDoorsByUsername(username)
                _doors.value = response.doors
            } catch (e: Exception) {
                _errorMessage.value = "Failed to load doors: ${e.message}"
            } finally {
                _isLoading.value = false
            }
        }
    }

    fun toggleAdminAccess(doorId: Int) {
        viewModelScope.launch {
            try {
                val response = api.toggleAdminAccess(doorId)
                if (response.success) {
                    _doors.update { list ->
                        list.map {
                            if (it.id == doorId) it.copy(allowAdminAccess = response.allowAdminAccess)
                            else it
                        }
                    }
                }
            } catch (e: Exception) {
                Log.e("App", "Failed toggling admin access: ${e.message}")
            }
        }
    }
}
