package com.ralphmarondev.pisync.features.home.presentation

import android.annotation.SuppressLint
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.History
import androidx.compose.material.icons.filled.Home
import androidx.compose.material.icons.filled.Settings
import androidx.compose.material.icons.outlined.History
import androidx.compose.material.icons.outlined.Home
import androidx.compose.material.icons.outlined.Settings
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.NavigationBar
import androidx.compose.material3.NavigationBarItem
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.text.style.TextOverflow
import com.ralphmarondev.pisync.features.history.presentation.HistoryScreen
import com.ralphmarondev.pisync.features.overview.presentation.OverviewScreen
import com.ralphmarondev.pisync.features.settings.presentation.overview.SettingScreen
import org.koin.androidx.compose.koinViewModel

@SuppressLint("UnusedMaterial3ScaffoldPaddingParameter")
@Composable
fun HomeScreen() {
    val viewModel: HomeViewModel = koinViewModel()
    val selectedIndex = viewModel.selectedIndex.collectAsState().value
    val navItems = listOf(
        NavItems(
            label = "Home",
            selectedIcon = Icons.Filled.Home,
            defaultIcon = Icons.Outlined.Home,
            onClick = { viewModel.onSelectedIndexValueChange(0) }
        ),
        NavItems(
            label = "History",
            selectedIcon = Icons.Filled.History,
            defaultIcon = Icons.Outlined.History,
            onClick = { viewModel.onSelectedIndexValueChange(1) }
        ),
        NavItems(
            label = "Settings",
            selectedIcon = Icons.Filled.Settings,
            defaultIcon = Icons.Outlined.Settings,
            onClick = { viewModel.onSelectedIndexValueChange(2) }
        )
    )

    Scaffold(
        bottomBar = {
            NavigationBar {
                navItems.forEachIndexed { index, navItems ->
                    NavigationBarItem(
                        selected = index == selectedIndex,
                        icon = {
                            val imageVector = if (index == selectedIndex) {
                                navItems.selectedIcon
                            } else {
                                navItems.defaultIcon
                            }
                            Icon(
                                imageVector = imageVector,
                                contentDescription = navItems.label
                            )
                        },
                        onClick = navItems.onClick,
                        label = {
                            Text(
                                text = navItems.label,
                                maxLines = 1,
                                overflow = TextOverflow.Ellipsis,
                                color = MaterialTheme.colorScheme.secondary
                            )
                        }
                    )
                }
            }
        }
    ) {
        when (selectedIndex) {
            0 -> OverviewScreen()
            1 -> HistoryScreen()
            2 -> SettingScreen(
                logout = {}
            )
        }
    }
}

private data class NavItems(
    val label: String,
    val selectedIcon: ImageVector,
    val defaultIcon: ImageVector,
    val onClick: () -> Unit
)