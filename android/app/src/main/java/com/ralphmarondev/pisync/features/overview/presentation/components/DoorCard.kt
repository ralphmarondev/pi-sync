package com.ralphmarondev.pisync.features.overview.presentation.components

import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.ElevatedCard
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Switch
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
fun DoorCard(
    checked: Boolean,
    toggleChecked: () -> Unit,
    label: String,
    modifier: Modifier = Modifier
) {
    val borderColor = if (checked) {
        MaterialTheme.colorScheme.secondary
    } else {
        MaterialTheme.colorScheme.onSecondary
    }
    ElevatedCard(
        onClick = toggleChecked,
        modifier = modifier
            .border(1.dp, borderColor, RoundedCornerShape(8.dp))
    ) {
        Column(
            modifier = Modifier
                .padding(16.dp)
        ) {
            Text(
                text = label,
                fontSize = 18.sp,
                fontWeight = FontWeight.W600,
                maxLines = 1,
                overflow = TextOverflow.Ellipsis
            )
            Spacer(modifier = Modifier.height(8.dp))
            Switch(
                checked = checked,
                onCheckedChange = { toggleChecked() }
            )
        }
    }
}