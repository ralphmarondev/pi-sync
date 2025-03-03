package com.ralphmarondev.pisync.features.home.presentation.components

import android.widget.Toast
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.lazy.grid.items
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import com.ralphmarondev.pisync.features.home.domain.model.Door
import com.ralphmarondev.pisync.features.home.presentation.HomeViewModel

@Composable
fun DoorList(
    modifier: Modifier = Modifier,
    viewModel: HomeViewModel
) {
    val context = LocalContext.current
    val doorState by viewModel.doorState.collectAsState()

    val doors = listOf(
        Door(
            id = 1,
            label = "A14",
            status = doorState,
            onClick = {
                viewModel.toggleDoorState(
                    onResult = { response ->
                    }
                )
            }
        ),
        Door(
            id = 1,
            label = "A15",
            status = doorState,
            onClick = {
                viewModel.toggleDoorState(
                    onResult = { response ->
                    }
                )
            }
        ),
        Door(
            id = 1,
            label = "A16",
            status = doorState,
            onClick = {
                viewModel.toggleDoorState(
                    onResult = { response ->
                    }
                )
            }
        )
    )


    LazyVerticalGrid(
        modifier = modifier
            .fillMaxWidth(),
        columns = GridCells.Fixed(2),
        horizontalArrangement = Arrangement.spacedBy(8.dp),
        verticalArrangement = Arrangement.spacedBy(8.dp)
    ) {
        items(doors) { door ->
            DoorCard(
                checked = doorState,
                toggleChecked = {
                    viewModel.toggleDoorState { response ->
                        if (response.success) {
                            Toast.makeText(context, response.message, Toast.LENGTH_SHORT)
                                .show()
                        } else {
                            Toast.makeText(
                                context,
                                "Failed to toggle door.",
                                Toast.LENGTH_SHORT
                            ).show()
                        }
                    }
                },
                label = door.label,
                modifier = Modifier
                    .fillMaxWidth()
            )
        }
    }
}